"""STUB: effect not implemented — do not guess mechanics.
Torterra (DP7 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.dp import (
    dp7_torterra_11_crash_impact,
    dp7_torterra_11_land_shake,
    dp7_torterra_11_sunshine_song,
)

card = PokemonCardDef(guid='868e1f91-210a-53f7-af52-c8612c6546b0', key='DP7', name='com.direwolfdigital.cake.data.archetypes.pokemon.Torterra.Name', display_name='Torterra', searchable_by=['Torterra', 'Stage 2', 'Torterra'], subtypes=['Stage 2'], collector_number=11, set_code='DP7', rarity=Rarities.RareHolo, hp=140, elements=[PokemonTypes.FIGHTING], stage=PokemonStage.STAGE2, retreat_cost=4, weakness_type=PokemonTypes.WATER, resistance_type=PokemonTypes.LIGHTNING, resistance_amount=20, evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name', family_id=389, abilities=[Ability(title='Sunshine Song', game_text='Once during your turn (before your attack), when you play Torterra from your hand to evolve 1 of your Pokémon, you may choose as many of your Grass Pokémon in play as you like. For each Grass Pokémon you choose, search your deck for an Evolution card that evolves from that Pokémon and evolve it. Shuffle your deck afterward.', ability_type=AbilityTypes.POKE_POWER, effect=dp7_torterra_11_sunshine_song(), activation=Activations.ONCE_PER_TURN), Attack(title='Crash Impact', game_text='Torterra does 20 damage to itself. Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon, if any.', cost={PokemonTypes.COLORLESS: 2}, damage=60, effect=dp7_torterra_11_crash_impact()), Attack(title='Land Shake', game_text="During your opponent's next turn, when your opponent puts a Basic Pokémon from his or her hand onto his or her Bench, put 2 damage counters on that Pokémon.", cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2}, damage=80, effect=dp7_torterra_11_land_shake())])
