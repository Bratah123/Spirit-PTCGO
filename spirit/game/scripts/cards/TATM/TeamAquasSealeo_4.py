from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, bonus_if, active_is
from spirit.game.content.definitions import def_for


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


card = PokemonCardDef(
    guid="b0a8223e-9738-5d00-a33a-aa696517e2ba",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name",
    display_name="Team Aqua's Sealeo",
    searchable_by=["Team Aqua's Sealeo", "Stage 1", "TeamAquasSealeo"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Splatter",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(20, pool='any', count=1),
        ),
        Attack(
            title="Hail Storm",
            game_text="If your opponent's Active Pok\u00e9mon is a Team Magma Pok\u00e9mon, this attack does 60 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(active_is(lambda p: _team(p, "Magma")), 60),
        ),
    ],
)