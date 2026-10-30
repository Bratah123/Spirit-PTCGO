from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import has_tool
from spirit.game.content.definitions import def_for


def _has_garbotoxin(pokemon):
    d = def_for(pokemon.archetype_id)
    return any(getattr(a, "title", None) == "Garbotoxin"
               for a in (getattr(d, "abilities", None) or []))


class _GarbotoxinPassive(Passive):
    """With a Pokemon Tool attached to this Pokemon, every other Pokemon has
    no Abilities (except Garbotoxin)."""

    def blocks_abilities(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        return bool(holder is not None and has_tool(holder)
                    and not _has_garbotoxin(pokemon))


card = PokemonCardDef(
    guid="50b5a4d3-a0a7-55a1-bb43-afae39609b6b",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    family_id=568,
    abilities=[
        Ability(
            title="Garbotoxin",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, each Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities (except for Garbotoxin).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_GarbotoxinPassive(),
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)