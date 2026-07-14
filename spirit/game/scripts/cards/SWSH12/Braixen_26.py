from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard


def _is_serena_card(card):
    definition = def_for(getattr(card, "archetype_id", None) or "")
    return getattr(definition, "display_name", None) == "Serena"


card = PokemonCardDef(
    guid="df24acfb-0268-5a75-920d-ef3a6039bdef",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    display_name="Braixen",
    searchable_by=["Braixen", "Stage 1", "Braixen"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Flare Parade",
            game_text="This attack does 60 damage for each Serena card in your discard pile.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_discard("mine", _is_serena_card), 60),
        ),
    ],
)
