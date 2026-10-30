"""STUB: effect not implemented — do not guess mechanics.
Ariados (EX10 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import reactive_poison, spider_trap

card = PokemonCardDef(
    guid="3d71c266-f70d-5d5d-8d2e-c6acd87368cb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Reactive Poison",
            game_text="Does 10 damage plus 30 more damage for each Special Condition affecting the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=reactive_poison(10, 30),
        ),
        Attack(
            title="Spider Trap",
            game_text="The Defending Pok\u00e9mon is now Asleep and Poisoned. Before applying this effect, you may switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. If you do, the new Defending Pok\u00e9mon is now Asleep and Poisoned. Your opponent chooses the Defending Pok\u00e9mon to switch.",
            cost={PokemonTypes.GRASS: 1},
            # STUB: attack effect not implemented
            effect=spider_trap(),
        ),
    ],
)