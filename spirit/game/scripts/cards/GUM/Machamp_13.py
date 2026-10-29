from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.gum import directing_traffic

card = PokemonCardDef(
    guid="85415617-8a62-5b13-9658-15f45dd96bee",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="GUM",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=68,
    abilities=[
        Attack(
            title="Directing Traffic",
            game_text="Look at the top 5 cards of your deck and put them back in any order.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=directing_traffic,
        ),
        Attack(
            title="Cross Chop",
            game_text="Flip a coin. If heads, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(60),
        ),
    ],
)
