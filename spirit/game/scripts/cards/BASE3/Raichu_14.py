from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


card = PokemonCardDef(
    guid="9280aed3-0597-5602-a83c-632d214a3466",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BASE3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=26,
    abilities=[
        Attack(
            title="Gigashock",
            game_text="Choose 3 of your opponent's Benched Pok\u00e9mon and this attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If your opponent has fewer than 3 Benched Pok\u00e9mon, do the damage to each of them.",
            cost={PokemonTypes.LIGHTNING: 4},
            damage=30,
            effect=snipe_attack(10, count=3, also_base=True),
        ),
    ],
)
