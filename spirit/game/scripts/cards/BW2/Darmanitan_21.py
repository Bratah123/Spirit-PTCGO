from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus, condition_attack

card = PokemonCardDef(
    guid="a9103048-567f-5342-bb31-0757d847a1c4",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1", "Darmanitan"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Rock Smash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Fire Punch",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)