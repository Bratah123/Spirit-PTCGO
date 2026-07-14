from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.card_effects.support_common import search_to_bench, is_basic


def _falinks_named(p):
    d = def_for(p.archetype_id)
    return bool(d and d.display_name and "Falinks" in d.display_name)

card = PokemonCardDef(
    guid="9e23a960-4d99-50a7-a248-1874244c2d31",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic, count=2),
        ),
        Attack(
            title="Team Attack",
            game_text="This attack does 30 damage for each of your Benched Pok\u00e9mon that has \"Falinks\" in its name.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_bench("mine", pred=_falinks_named), 30),
        ),
    ],
)