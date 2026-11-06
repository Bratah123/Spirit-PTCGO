from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import high_voltage, stun_wave


card = PokemonCardDef(
    guid="94798715-fef9-5087-a3c7-def954125475",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkFlaaffy.Name",
    display_name="Dark Flaaffy",
    searchable_by=["Dark Flaaffy", "Stage 1", "DarkFlaaffy"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="High Voltage",
            game_text="Flip a coin. If heads, your opponent can't play Trainer cards during his or her next turn.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=high_voltage,
        ),
        Attack(
            title="Stun Wave",
            game_text="If the Defending Pok\u00e9mon has a Pok\u00e9mon Power, that power stops working until the end of your next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=stun_wave,
        ),
    ],
)
