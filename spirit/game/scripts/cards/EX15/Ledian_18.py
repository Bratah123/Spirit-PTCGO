"""STUB: effect not implemented — do not guess mechanics.
Ledian δ (EX15 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import metal_star_draw_if_tool, prowl_on_evolve_any_card
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="50e83a3b-6564-5707-a4e9-2ca345ac3178",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian δ",
    searchable_by=["Ledian \u03b4", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX15",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=166,
    abilities=[
        Ability(
            title="Prowl",
            game_text="Once during your turn, when you play Ledian from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=prowl_on_evolve_any_card(),
        ),
        Attack(
            title="Metal Star",
            game_text="If Ledian has a Pok\u00e9mon Tool card attached to it, draw 3 cards.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=metal_star_draw_if_tool(3),
        ),
    ],
)