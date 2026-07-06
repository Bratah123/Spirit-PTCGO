from spirit.game.card_effects.pokemon import shady_dealings
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f776e12a-85c1-5fd4-b9b2-02198c15bbe8",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Inteleon.Name",
    display_name="Inteleon",
    searchable_by=["Inteleon", "Stage 2", "Inteleon"],
    subtypes=["Stage 2"],
    collector_number=58,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    family_id=816,
    abilities=[
        Ability(
            title="Shady Dealings",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may search your deck for up to 2 Trainer cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=shady_dealings(2),
        ),
        Attack(
            title="Aqua Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)