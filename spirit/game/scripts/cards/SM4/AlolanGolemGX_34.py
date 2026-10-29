from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import heavy_rock_gx, super_electromagnetic_tackle

card = PokemonCardDef(
    guid="aadf35e1-fbcb-57b7-873c-f04a7ff0a909",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolemGX.Name",
    display_name="Alolan Golem-GX",
    searchable_by=["Alolan Golem-GX", "Stage 2", "GX", "AlolanGolemGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=34,
    set_code="SM4",
    rarity=Rarities.RareHoloGX,
    hp=250,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Super Electromagnetic Tackle",
            game_text="This Pok\u00e9mon does 50 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=super_electromagnetic_tackle,
        ),
        Attack(
            title="Heavy Rock-GX",
            game_text="Your opponent can't play any cards from their hand during their next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=heavy_rock_gx,
        ),
    ],
)