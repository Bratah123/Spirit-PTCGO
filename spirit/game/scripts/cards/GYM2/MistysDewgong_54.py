from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, recoil_attack
from spirit.game.card_effects.ecard import defender_has_type


card = PokemonCardDef(
    guid="50b79a97-2949-5632-a867-3717d18c8d1c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysDewgong.Name",
    display_name="Misty's Dewgong",
    searchable_by=["Misty's Dewgong", "Stage 1", "MistysDewgong"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysSeel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Ice Throw",
            game_text="If the Defending Pok\u00e9mon is Fighting, this attack's base damage is doubled.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=bonus_if(defender_has_type(PokemonTypes.FIGHTING), 20),
        ),
        Attack(
            title="Take Down",
            game_text="Misty's Dewgong does 20 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=recoil_attack(20),
        ),
    ],
)
