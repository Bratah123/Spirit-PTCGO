from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.ecard import poison_needle_rush


card = PokemonCardDef(
    guid="ba1d0dc6-9a54-53dd-81eb-d9c1180cb05f",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1", "Sandslash"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Sand Trap",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose up to 2 of them. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=snipe_attack(10, pool="bench", count=2, also_base=True, optional=True),
        ),
        Attack(
            title="Poison Needle Rush",
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads. If you get at least 1 heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=poison_needle_rush,
        ),
    ],
)
