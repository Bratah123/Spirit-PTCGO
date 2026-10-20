from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


def _is_combee(card):
    d = def_for(card.archetype_id)
    return is_pokemon_card(card) and getattr(d, "display_name", "") == "Combee"


card = PokemonCardDef(
    guid="28c68674-f7ec-5dba-8713-16ca77214fc8",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name",
    display_name="Vespiquen",
    searchable_by=["Vespiquen", "Stage 1", "Vespiquen"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name",
    family_id=415,
    abilities=[
        Attack(
            title="Gather Order",
            game_text="Search your deck for as many Combee as you like and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_bench(_is_combee, count=5, prompt="Choose any number of Combee"),
        ),
        Attack(
            title="Damage Beat",
            game_text="Does 20 damage times the number of damage counters on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on('defender'), 20),
        ),
    ],
)