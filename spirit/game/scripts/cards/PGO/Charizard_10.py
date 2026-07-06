from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0102ad8f-c8f6-5a87-ad03-66c7fe4282b3",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Burn Brightly",
            game_text="Each basic Fire Energy attached to your Pok\u00e9mon provides FireFire Energy. You can't apply more than 1 Burn Brightly Ability at a time.",
            effect=unimplemented,
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)