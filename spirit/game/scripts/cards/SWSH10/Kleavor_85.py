from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench, recoil_attack

card = PokemonCardDef(
    guid="3ffacdb3-a8a6-5cd8-97ba-6608c4bf837b",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kleavor.Name",
    display_name="Kleavor",
    searchable_by=["Kleavor", "Stage 1", "Kleavor"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="SWSH10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Rout",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), 30, base=10),
        ),
        Attack(
            title="Rocky Tackle",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=recoil_attack(50),
        ),
    ],
)