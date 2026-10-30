"""STUB: effect not implemented — do not guess mechanics.
Medicham (EX5 #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import chakra_points, meditate_damage

card = PokemonCardDef(
    guid="3815d22c-05e6-543d-9806-a6a2f4360953",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1", "Medicham"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Meditate",
            game_text="Does 20 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=meditate_damage(20, 10),
        ),
        Attack(
            title="Chakra Points",
            game_text="Does 10 damage plus 10 more damage for each card in your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=chakra_points(10, 10),
        ),
    ],
)