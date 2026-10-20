from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="4912e94b-2b17-5c68-bceb-6a80d1c55701",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    display_name="Prinplup",
    searchable_by=["Prinplup", "Stage 1", "Prinplup"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    family_id=393,
    abilities=[
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)