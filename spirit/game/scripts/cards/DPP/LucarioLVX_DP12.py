"""DP2 Mysterious Treasures — wired.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    close_combat,
    stance_passive,
)

card = PokemonCardDef(guid='4e652077-5824-5b86-9a1b-4587a102bf57', key='DP2', name='com.direwolfdigital.cake.data.archetypes.pokemon.LucarioLVX.Name', display_name='Lucario LV.X', searchable_by=['Lucario LV.X', 'Level-Up', 'LucarioLVX'], subtypes=['Level-Up'], collector_number=12, set_code='DP2', rarity=Rarities.RareHolo, hp=110, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.LEVELUP, retreat_cost=1, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name', family_id=448, abilities=[Ability(title='Stance', game_text="Once during your turn (before your attack), when you put Lucario LV.X from your hand onto your Active Lucario, you may use this power. Prevent all effects of an attack, including damage, done to Lucario during your opponent's next turn. (If Lucario is no longer your Active Pokémon, this effect ends.)", ability_type=AbilityTypes.POKE_POWER, passive=stance_passive(), activation=Activations.ONCE_PER_TURN), Attack(title='Close Combat', game_text="During your opponent's next turn, any damage done to Lucario by attacks is increased by 30 (after applying Weakness and Resistance).", cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1}, damage=80, effect=close_combat(80, 30))])
