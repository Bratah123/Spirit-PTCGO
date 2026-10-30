"""STUB: effect not implemented — do not guess mechanics.
Infernape (DP7 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_infernape_3_blaze_dance,
    dp7_infernape_3_close_combat,
    dp7_infernape_3_spreading_fire,
)

card = PokemonCardDef(guid='d747158b-b9db-5359-80df-063e43068334', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name', display_name='Infernape', searchable_by=['Infernape', 'Stage 2', 'Infernape'], subtypes=['Stage 2'], collector_number=3, set_code='DP7', rarity=Rarities.RareHolo, hp=120, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=0, weakness_type=PokemonTypes.PSYCHIC, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name', family_id=392, abilities=[Ability(title='Blaze Dance', game_text='Once during your turn (before your attack), when you play Infernape from your hand to evolve 1 of your Pokémon, you may flip a coin. If heads, search your deck for up to 4 Fire Energy cards and attach them to your Pokémon in any way you like. Shuffle your deck afterward.', ability_type=AbilityTypes.POKE_POWER, effect=dp7_infernape_3_blaze_dance(), activation=Activations.ONCE_PER_TURN), Attack(title='Close Combat', game_text="During your opponent's next turn, any damage done to Infernape by attacks is increased by 30 (after applying Weakness and Resistance).", cost={PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_infernape_3_close_combat()), Attack(title='Spreading Fire', game_text="Discard 2 Fire Energy attached to Infernape and this attack does 20 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)", cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=dp7_infernape_3_spreading_fire())])
