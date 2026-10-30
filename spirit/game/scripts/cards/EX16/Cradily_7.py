"""STUB: effect not implemented — do not guess mechanics.
Cradily (EX16 #7): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import evolutionary_call_search, poison_ring


card = PokemonCardDef(
    guid="c90c2f2f-0f48-5359-a36c-5234c9ebd202",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 2", "Cradily"],
    subtypes=["Stage 2"],
    collector_number=7,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Ability(
            title="Evolutionary Call",
            game_text="Once during your turn, when you play Cradily from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for up to 3 in any combination of Basic Pok\u00e9mon or Evolution cards. Show them to your opponent and put them into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=evolutionary_call_search(3),
        ),
        Attack(
            title="Poison Ring",
            game_text="The Defending Pok\u00e9mon is now Poisoned. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            # STUB: attack effect not implemented
            effect=poison_ring(),
        ),
    ],
)