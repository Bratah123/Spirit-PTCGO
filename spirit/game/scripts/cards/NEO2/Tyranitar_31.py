from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import trample


card = PokemonCardDef(
    guid="acd2d6c8-336c-5954-96fe-194e37ce37f2",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar",
    searchable_by=["Tyranitar", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="NEO2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Trample",
            game_text="For each Benched Pok\u00e9mon in play (yours and your opponent's), flip a coin. If heads, this attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=trample(30),
        ),
    ],
)
