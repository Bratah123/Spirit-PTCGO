from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import whirlwind


card = PokemonCardDef(
    guid="8e888168-036c-582e-9de1-174328c48d59",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name",
    display_name="Pidgeotto",
    searchable_by=["Pidgeotto", "Stage 1", "Pidgeotto"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="If your opponent has any Benched Pok\u00e9mon, he or she chooses 1 of them and switches the Defending Pok\u00e9mon with it. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=whirlwind,
        ),
    ],
)
