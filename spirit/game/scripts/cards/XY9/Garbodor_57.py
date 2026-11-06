from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import has_tool, condition_attack
from spirit.game.content.definitions import def_for


class _GarbotoxinPassive(Passive):
    """With a Pokemon Tool attached to this Pokemon, every other Pokemon has
    no Abilities (except Garbotoxin)."""

    def blocks_abilities(self, pokemon, carrier):
        holder = carrier_pokemon(carrier)
        return bool(holder is not None and has_tool(holder)
                    and not _has_garbotoxin(pokemon))


def _has_garbotoxin(pokemon):
    d = def_for(pokemon.archetype_id)
    return any(getattr(a, "title", None) == "Garbotoxin"
               for a in (getattr(d, "abilities", None) or []))


card = PokemonCardDef(
    guid="90a4463b-49ec-5bd0-93c4-7bd0a758bd9a",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garbodor.Name",
    display_name="Garbodor",
    searchable_by=["Garbodor", "Stage 1", "Garbodor"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="XY9",
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
            passive=_GarbotoxinPassive(),
        ),
        Attack(
            title="Offensive Bomb",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)