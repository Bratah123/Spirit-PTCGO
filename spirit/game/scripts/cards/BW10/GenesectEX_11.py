from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="7bccf330-088d-53ce-9ae0-a724621cccbb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GenesectEX.Name",
    display_name="Genesect-EX",
    searchable_by=["Genesect-EX", "Basic", "EX", "Team Plasma", "GenesectEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=11,
    set_code="BW10",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=649,
    abilities=[
        Ability(
            title="Red Signal",
            game_text="When you attach a Plasma Energy from your hand to this Pok\u00e9mon, you may switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Megalo Cannon",
            game_text="Does 20 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness or Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)