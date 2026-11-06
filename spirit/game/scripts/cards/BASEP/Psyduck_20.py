from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import headache


card = PokemonCardDef(
    guid="f107a48b-e23a-535d-97dd-173e25b05e04",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Headache",
            game_text="Your opponent can't play Trainer cards during his or her next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=headache,
        ),
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)
