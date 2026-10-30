from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import twister_attack

card = PokemonCardDef(
    guid="d7a72bd4-dcd7-5192-8a0a-fa35ad7ac32a",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyaradosex.Name",
    display_name="Gyarados ex",
    searchable_by=["Gyarados ex", "Stage 1", "ex", "Gyaradosex"],
    subtypes=["Stage 1", "ex"],
    collector_number=109,
    set_code="EX6",
    rarity=Rarities.RareHoloEX,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, choose 1 Energy attached to the Defending Pok\u00e9mon, if any, and discard it. If both are tails, this attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=twister_attack(40),
        ),
        Attack(
            title="Dragon Rage",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)