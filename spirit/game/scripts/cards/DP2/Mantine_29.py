"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    giant_wave,
    jumbo_fin_passive,
)

card = PokemonCardDef(guid='a147e24a-6153-5e92-be30-25719404e5ac', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name', display_name='Mantine', searchable_by=['Mantine', 'Basic', 'Mantine'], subtypes=['Basic'], collector_number=29, set_code='DP2', rarity=Rarities.Rare, hp=80, elements=[PokemonTypes.WATER], stage=PokemonStage.BASIC, retreat_cost=1, weakness_type=PokemonTypes.LIGHTNING, resistance_type=PokemonTypes.FIGHTING, resistance_amount=20, family_id=226, abilities=[Ability(title='Jumbo Fin', game_text='If Mantyke is anywhere under Mantine, the Retreat Cost for each of your Water Pokémon is ColorlessColorless less.', ability_type=AbilityTypes.POKE_BODY, passive=jumbo_fin_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Giant Wave', game_text="Mantine can't use Giant Wave during your next turn.", cost={PokemonTypes.WATER: 2}, damage=50, effect=giant_wave(50))])
