from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import bonus_if, active_is


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


class _SludgeFestival(Passive):
    """The Retreat Cost of each Pokemon in play (except Team Aqua Pokemon) is Colorless more."""
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return cost if _team(pokemon, "Aqua") else cost + 1


def _affected(p):
    return p is not None and bool(p.get_attribute(AttrID.SPECIAL_CONDITIONS))


card = PokemonCardDef(
    guid="bb708c3d-9b16-5e11-ab22-da791206dcde",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMuk.Name",
    display_name="Team Aqua's Muk",
    searchable_by=["Team Aqua's Muk", "Stage 1", "TeamAquasMuk"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sludge Festival",
            game_text="The Retreat Cost of each Pok\u00e9mon in play (except for Team Aqua Pok\u00e9mon) is Colorless more.",
            passive=_SludgeFestival(),
        ),
        Attack(
            title="Pester",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(active_is(_affected), 60),
        ),
    ],
)