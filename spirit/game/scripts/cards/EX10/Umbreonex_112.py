"""STUB: effect not implemented — do not guess mechanics.
Umbreon ex (EX10 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Triggers, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import darker_ring_on_evolve, black_cry_lock

card = PokemonCardDef(
    guid="036787b9-f909-5ef2-b33c-c88639850dce",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name",
    display_name="Umbreon ex",
    searchable_by=["Umbreon ex", "Stage 1", "ex", "Umbreonex"],
    subtypes=["Stage 1", "ex"],
    collector_number=112,
    set_code="EX10",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Darker Ring",
            game_text="Once during your turn (before your attack), when you play Umbreon ex from your hand to evolve 1 of your Pok\u00e9mon, switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            # STUB: ability effect not implemented
            effect=darker_ring_on_evolve(),
        ),
        Attack(
            title="Black Cry",
            game_text="The Defending Pok\u00e9mon can't retreat or use any Pok\u00e9-Powers during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=black_cry_lock(),
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)