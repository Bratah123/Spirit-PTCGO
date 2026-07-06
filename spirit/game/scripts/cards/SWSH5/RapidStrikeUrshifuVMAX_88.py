from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f732bc5c-f93c-5290-bb63-ca77e024d80a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuVMAX.Name",
    display_name="Rapid Strike Urshifu VMAX",
    searchable_by=["Rapid Strike Urshifu VMAX", "VMAX", "Rapid Strike", "RapidStrikeUrshifuVMAX"],
    subtypes=["VMAX", "Rapid Strike"],
    collector_number=88,
    set_code="SWSH5",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name",
    family_id=892,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="G-Max Rapid Flow",
            game_text="Discard all Energy from this Pok\u00e9mon. This attack does 120 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)