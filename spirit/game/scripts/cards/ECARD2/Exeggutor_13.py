from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage
from spirit.game.card_effects.ecard import count_benched_energy


card = PokemonCardDef(
    guid="d733dc1c-edce-5933-a2e9-50797edcec0f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggutor.Name",
    display_name="Exeggutor",
    searchable_by=["Exeggutor", "Stage 1", "Exeggutor"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Big Eggsplosion",
            game_text="Flip a number of coins equal to the amount of Energy attached to Exeggutor. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins_from=count_energy("self"), per_heads=20),
        ),
        Attack(
            title="Lateral Eggsplosion",
            game_text="Flip a number of coins equal to the amount of Energy attached to all of of your Benched Pok\u00e9mon. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins_from=count_benched_energy, bonus_per_heads=10),
        ),
    ],
)
