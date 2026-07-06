from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54612974-e4ee-5bff-86c8-fb5a59135b84",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoVSTAR.Name",
    display_name="Mewtwo VSTAR",
    searchable_by=["Mewtwo VSTAR", "VSTAR", "MewtwoVSTAR"],
    subtypes=["VSTAR"],
    collector_number=86,
    set_code="PGO",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoV.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Psy Purge",
            game_text="Discard up to 3 Psychic Energy from your Pok\u00e9mon. This attack does 90 damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Star Raid",
            game_text="This attack does 120 damage to each of your opponent's Pok\u00e9mon V. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)