"""STUB: effect not implemented — do not guess mechanics.
Meganium δ (EX15 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import delta_reduction_next, evolutionary_call_search
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="3fcc4658-9699-5852-9f76-2a81996bad6c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium δ",
    searchable_by=["Meganium \u03b4", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX15",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=154,
    abilities=[
        Ability(
            title="Evolutionary Call",
            game_text="Once during your turn, when you play Meganium from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for up to 3 in any combination of Basic Pok\u00e9mon or Evolution cards. Show them to your opponent and put them into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=evolutionary_call_search(3),
        ),
        Attack(
            title="Delta Reduction",
            game_text="During your opponent's next turn, any damage done by attacks from the Defending Pok\u00e9mon is reduced by 30 (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=delta_reduction_next(30),
        ),
        Attack(
            title="Mega Impact",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)