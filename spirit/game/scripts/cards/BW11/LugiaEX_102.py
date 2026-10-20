from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="971a7254-fbb8-5317-a3c7-0ba24364fe45",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaEX.Name",
    display_name="Lugia-EX",
    searchable_by=["Lugia-EX", "Basic", "EX", "Team Plasma", "LugiaEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=102,
    set_code="BW11",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Overflow",
            game_text="If your opponent's Pok\u00e9mon is Knocked Out by damage from an attack of this Pok\u00e9mon, take 1 more Prize card.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Plasma Gale",
            game_text="Discard a Plasma Energy attached to this Pok\u00e9mon. If you can't discard a Plasma Energy, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=unimplemented,
        ),
    ],
)