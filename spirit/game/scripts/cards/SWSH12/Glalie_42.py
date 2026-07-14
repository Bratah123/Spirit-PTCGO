from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if


def _played_candice(ctx):
    return ctx.played_trainer_this_turn("Candice") > 0


card = PokemonCardDef(
    guid="08abe688-454d-5dcd-bc3e-c6ae1bdf140e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Big Mouth",
            game_text="If you played Candice from your hand during this turn, this attack does 130 more damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            damage_operator="+",
            effect=bonus_if(_played_candice, 130),
        ),
    ],
)