from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, count_energy

card = PokemonCardDef(
    guid="0c1d09a6-9685-5ba2-aa13-f414802c6d37",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    display_name="Dewott",
    searchable_by=["Dewott", "Stage 1", "Dewott"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    family_id=501,
    abilities=[
        Attack(
            title="Aqua Tail",
            game_text="Flip a coin for each Water Energy attached to this Pok\u00e9mon. This attack does 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", energy_type=PokemonTypes.WATER),
                bonus_per_heads=10,
            ),
        ),
    ],
)
