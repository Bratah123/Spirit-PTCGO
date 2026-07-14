from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench

card = PokemonCardDef(
    guid="43b577aa-2ead-5c2a-bf8b-ada729bca129",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxVMAX.Name",
    display_name="Snorlax VMAX",
    searchable_by=["Snorlax VMAX", "VMAX", "SnorlaxVMAX"],
    subtypes=["VMAX"],
    collector_number=142,
    set_code="SWSH1",
    rarity=Rarities.RareHoloVMAX,
    hp=340,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxV.Name",
    family_id=143,
    abilities=[
        Attack(
            title="G-Max Fall",
            game_text="This attack does 30 more damage for each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_bench("mine"), 30, base=60),
        ),
    ],
)