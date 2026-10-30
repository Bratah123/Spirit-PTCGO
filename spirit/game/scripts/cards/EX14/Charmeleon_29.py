from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flamethrower_discard_fire, rage_damage

card = PokemonCardDef(
    guid="d8aaf881-7817-5c10-bdc3-87536d54246b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    display_name="Charmeleon",
    searchable_by=["Charmeleon", "Stage 1", "Charmeleon"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Charmeleon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
                        effect=rage_damage(10, 10),
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard a Fire Energy attached to Charmeleon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
                        effect=flamethrower_discard_fire(),
        ),
    ],
)