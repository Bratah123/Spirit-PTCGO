from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack


card = PokemonCardDef(
    guid="b801718f-0f0e-5c70-98c0-cf4fe364e019",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slurpuff.Name",
    display_name="Slurpuff",
    searchable_by=["Slurpuff", "Stage 1", "Slurpuff"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    family_id=684,
    abilities=[
        Attack(
            title="Lap Up",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.FAIRY: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)