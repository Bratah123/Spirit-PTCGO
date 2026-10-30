"""EX13 Holon Phantoms — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import (
    power_blow_per_energy,
    splash_back_return_bench,
)

card = PokemonCardDef(guid='ee9efad5-3279-5e7e-add5-655837d5a835', key='EX13', name='com.direwolfdigital.cake.data.archetypes.pokemon.Crawdauntex.Name', display_name='Crawdaunt ex', searchable_by=['Crawdaunt ex', 'Stage 1', 'ex', 'Crawdauntex'], subtypes=['Stage 1', 'ex'], collector_number=99, set_code='EX13', rarity=Rarities.RareHoloEX, hp=110, elements=[PokemonTypes.WATER], stage=PokemonStage.STAGE1, retreat_cost=2, weakness_type=PokemonTypes.LIGHTNING, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name', family_id=341, abilities=[Ability(title='Splash Back', game_text="Once during your turn (before your attack), if your opponent has 4 or more Benched Pokémon, you may choose 1 of them and return that Pokémon and all cards attached to it to his or her hand. This power can't be used if Crawdaunt ex is affected by a Special Condition.", ability_type=AbilityTypes.POKE_POWER, effect=splash_back_return_bench(), activation=Activations.ONCE_PER_TURN), Attack(title='Power Blow', game_text='Does 20 damage times the amount of Energy attached to Crawdaunt ex.', cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1}, damage=20, damage_operator='x', effect=power_blow_per_energy(20))])
