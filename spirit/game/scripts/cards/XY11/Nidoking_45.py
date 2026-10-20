from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.attacks_common import damage_per, count_bench
from spirit.game.session.effects import is_basic_pokemon, is_restored_pokemon


def _named(p, name):
    return getattr(def_for(p.archetype_id), "display_name", None) == name


def _is_evolution(p):
    return not is_basic_pokemon(p) and not is_restored_pokemon(p)


card = PokemonCardDef(
    guid="eff15dce-c705-5284-9c93-ca049ecfb296",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name",
    display_name="Nidoking",
    searchable_by=["Nidoking", "Stage 2", "Nidoking"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name",
    family_id=32,
    abilities=[
        Ability(
            title="King's Palace",
            game_text="Your Nidoqueen's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=lambda p: _named(p, "Nidoqueen")),
        ),
        Attack(
            title="Power Lariat",
            game_text="This attack does 30 more damage for each Evolution Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench("mine", _is_evolution), 30, base=60),
        ),
    ],
)