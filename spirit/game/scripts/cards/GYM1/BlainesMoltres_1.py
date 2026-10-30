from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import phoenix_flame


card = PokemonCardDef(
    guid="d7c6a56a-5214-576d-b184-3f23a6c58fce",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesMoltres.Name",
    display_name="Blaine's Moltres",
    searchable_by=["Blaine's Moltres", "Basic", "BlainesMoltres"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Phoenix Flame",
            game_text="Flip a coin. If tails, shuffle Blaine's Moltres and all cards attached to it into your deck (after doing damage).",
            cost={PokemonTypes.FIRE: 5},
            damage=90,
            effect=phoenix_flame,
        ),
    ],
)
