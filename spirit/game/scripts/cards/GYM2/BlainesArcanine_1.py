from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack, self_energy_discard_attack
from spirit.game.card_effects.ecard import has_typed_basic_energy


card = PokemonCardDef(
    guid="8926bf44-ee31-5d6e-90db-05e4907c63dd",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesArcanine.Name",
    display_name="Blaine's Arcanine",
    searchable_by=["Blaine's Arcanine", "Stage 1", "BlainesArcanine"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="Blaine's Arcanine does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=recoil_attack(10),
        ),
        Attack(
            title="Firestorm",
            game_text="Discard 3 Fire Energy cards attached to Blaine's Arcanine in order to use this attack.",
            cost={PokemonTypes.FIRE: 4},
            damage=120,
            condition=has_typed_basic_energy(PokemonTypes.FIRE, 3),
            effect=self_energy_discard_attack(
                count=3, energy_type=PokemonTypes.FIRE),
        ),
    ],
)
