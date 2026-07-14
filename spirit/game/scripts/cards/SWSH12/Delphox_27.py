from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_discard, count_energy


def _is_serena_card(card):
    definition = def_for(card.archetype_id)
    return bool(definition and (definition.display_name or "") == "Serena")


card = PokemonCardDef(
    guid="8ba6ad51-dee9-5ae8-9411-399283a51c82",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Attack(
            title="Flare Parade",
            game_text="This attack does 60 damage for each Serena card in your discard pile.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_discard("mine", _is_serena_card), 60),
        ),
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 50),
        ),
    ],
)
