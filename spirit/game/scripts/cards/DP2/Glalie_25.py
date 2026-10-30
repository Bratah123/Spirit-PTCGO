"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    craggy_face_passive,
    intimidation_pebble,
)

card = PokemonCardDef(guid='e85329a7-76cb-5e99-adde-1a2c31a606ce', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name', display_name='Glalie', searchable_by=['Glalie', 'Stage 1', 'Glalie'], subtypes=['Stage 1'], collector_number=25, set_code='DP2', rarity=Rarities.Rare, hp=90, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.METAL, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name', family_id=361, abilities=[Ability(title='Craggy Face', game_text="As long as Glalie is your Active Pokémon, any damage done by attacks from your opponent's Stage 2 Evolved Pokémon is reduced by 20 (before applying Weakness and Resistance).", ability_type=AbilityTypes.POKE_BODY, passive=craggy_face_passive(20), activation=Activations.ONCE_PER_TURN), Attack(title='Intimidation Pebble', game_text="Flip a coin. If heads, your opponent can't play any Trainer cards or Supporter cards from his or her hand during your opponent's next turn.", cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1}, damage=50, effect=intimidation_pebble(50))])
