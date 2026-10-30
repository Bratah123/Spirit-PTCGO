from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import smash_turn, water_gun_extra

card = PokemonCardDef(
    guid="65c2a661-5bef-5d5c-b3ea-600187f35ba6",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    display_name="Wartortle",
    searchable_by=["Wartortle", "Stage 1", "Wartortle"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    family_id=7,
    abilities=[
        Attack(
            title="Water Gun",
            game_text="Does 20 damage plus 10 more damage for each Water Energy attached to Wartortle but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="+",
            effect=water_gun_extra(20, 10),
        ),
        Attack(
            title="Smash Turn",
            game_text="After your attack, you may switch Wartortle with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=smash_turn(),
        ),
    ],
)