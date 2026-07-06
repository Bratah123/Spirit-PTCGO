from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import teraspark

card = PokemonCardDef(
    guid="7340019a-e70e-522f-834f-550443cfa747",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regieleki.Name",
    display_name="Regieleki",
    searchable_by=["Regieleki", "Basic", "Regieleki"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=894,
    abilities=[
        Attack(
            title="Static Shock",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Teraspark",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon. This attack also does 40 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=teraspark,
        ),
    ],
)
