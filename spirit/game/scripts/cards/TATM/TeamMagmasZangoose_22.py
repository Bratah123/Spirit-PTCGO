from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import damage_per, count_bench


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


card = PokemonCardDef(
    guid="832fc007-ff56-594b-9af7-f7b47447eabd",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasZangoose.Name",
    display_name="Team Magma's Zangoose",
    searchable_by=["Team Magma's Zangoose", "Basic", "TeamMagmasZangoose"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Team Magma Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(lambda c: is_basic_pokemon(c) and _team(c, "Magma"), 2, prompt="Choose up to 2 Basic Team Magma Pokémon"),
        ),
        Attack(
            title="Team Play",
            game_text="This attack does 20 damage times the number of Team Magma Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_bench("mine", lambda p: _team(p, "Magma")), 20),
        ),
    ],
)