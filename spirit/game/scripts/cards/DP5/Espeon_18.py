"""DP5 Majestic Dawn — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp5_espeon_18_morning_sun,
    dp5_espeon_18_sunlight_veil,
)

card = PokemonCardDef(guid='0a58cb61-8572-58d1-8145-f52661eda2fd', key='DP5', name='com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name', display_name='Espeon', searchable_by=['Espeon', 'Stage 1', 'Espeon'], subtypes=['Stage 1'], collector_number=18, set_code='DP5', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.PSYCHIC], stage=PokemonStage.STAGE1, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name', family_id=133, abilities=[Ability(title='Sunlight Veil', game_text="Each of your Pokémon that evolves from Eevee gets +20 HP. You can't use more than 1 Sunlight Veil Poké-Body each turn.", ability_type=AbilityTypes.POKE_BODY, passive=dp5_espeon_18_sunlight_veil(), activation=Activations.ONCE_PER_TURN), Attack(title='Morning Sun', game_text='You may move an Energy card attached to Espeon to 1 of your Benched Pokémon.', cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2}, damage=60, effect=dp5_espeon_18_morning_sun())])
