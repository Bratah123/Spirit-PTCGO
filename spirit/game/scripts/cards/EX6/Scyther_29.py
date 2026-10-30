from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import fury_cutter, leaf_ride_passive

card = PokemonCardDef(
    guid="5d2369b0-72ab-5f3b-be76-609d9bc13403",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    display_name="Scyther",
    searchable_by=["Scyther", "Basic", "Scyther"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=123,
    abilities=[
        Ability(
            title="Leaf Ride",
            game_text="If Scyther has any Energy attached to it, Scyther's Retreat Cost is 0.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=leaf_ride_passive(),
        ),
        Attack(
            title="Fury Cutter",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 10 damage plus 10 more damage. If 2 of them are heads, this attack does 10 damage plus 20 more damage. If all of them are heads, this attack does 10 damage plus 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=fury_cutter(10, 10, 20, coins=3),
        ),
    ],
)