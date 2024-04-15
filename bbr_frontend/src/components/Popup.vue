<template>
	<div class="fixed top-0 left-0 right-0 bottom-0 z-50 bg-black bg-opacity-20 flex items-center justify-center">
		<div class="bg-white p-8">
			<slot />
			<button class="popup-close" @click="TogglePopup()">
				Close Popup
			</button>
		</div>
	</div>
</template>

<script>
export default {
	props: ['TogglePopup']
}
</script>
